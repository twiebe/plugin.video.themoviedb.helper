from tmdbhelper.lib.items.database.baseview_factories.concrete_classes.castmember import CastMemberMediaList
from jurialmunkey.ftools import cached_property


class CrewMemberMediaList(CastMemberMediaList):
    table = 'crewmember'
    cached_data_base_conditions = 'parent_id=? AND expiry>=? AND datalevel>=?'  # WHERE conditions
    cached_data_check_key = 'parent_id'
    group_by = 'crewmember.tmdb_id'
    keys = ('GROUP_CONCAT(role, " / ") as role', 'department', 'appearances', 'parent_id')

    order_by_direction_fallback = 'ASC'

    # Jobs listed first, one tuple per rank: writers, directors, then producers by seniority
    crew_order_roles = (
        (
            'Writer', 'Screenplay', 'Teleplay', 'Story', 'Original Story', 'Novel', 'Author',
            'Book', 'Short Story', 'Comic Book', 'Graphic Novel', 'Characters', 'Theatre Play',
            'Musical', 'Original Concept', 'Idea', 'Adaptation', 'Co-Writer', 'Creator',
            'Original Series Creator'),
        ('Director',),
        ('Co-Director',),
        ('Producer',),
        ('Executive Producer',),
        (
            'Co-Producer', 'Co-Executive Producer', 'Associate Producer', 'Line Producer',
            'Supervising Producer', 'Consulting Producer', 'Coordinating Producer'),
    )

    # Everyone else by department, then job
    crew_order_departments = (
        'Directing', 'Writing', 'Production', 'Camera', 'Editing', 'Sound', 'Art',
        'Costume & Make-Up', 'Visual Effects', 'Lighting', 'Crew',
    )

    @staticmethod
    def get_sql_strings(values):
        return ', '.join(f"'{v}'" for v in values)

    def get_crew_order_role_ranks(self):
        return ' '.join(
            f"WHEN role IN ({self.get_sql_strings(roles)}) THEN '{x:02d}'"
            for x, roles in enumerate(self.crew_order_roles))

    def get_crew_order_department_ranks(self):
        return ' '.join(
            f"WHEN '{department}' THEN '{x:02d}'"
            for x, department in enumerate(self.crew_order_departments))

    def get_crew_order_key(self):
        """ Text key of a job: its rank, or department and job for the rest, then the name """
        return (
            f'CASE {self.get_crew_order_role_ranks()} '
            f"ELSE '99' || CASE department {self.get_crew_order_department_ranks()} ELSE '99' END || LOWER(role) "
            f'END || CHAR(1) || LOWER(creditedperson.name)')

    @cached_property
    def sort_by_fallback(self):
        """ A person with several jobs sorts by their highest ranked job """
        return f'MIN({self.get_crew_order_key()})'

    filter_key_map = {
        'role': 'role',
        'department': 'department',
        'appearances': 'appearances',
        'title': 'creditedperson.name',
        'gender': 'creditedperson.gender',
    }

    @staticmethod
    def map_item_infoproperties(i):
        return {
            'role': i['role'],
            'job': i['role'],
            'department': i['department'],
            'tmdb_id': i['tmdb_id'],
            'tmdb_type': 'person',
        }


class Movie(CrewMemberMediaList):
    pass


class Tvshow(CrewMemberMediaList):
    pass


class Season(CrewMemberMediaList):
    @cached_property
    def item_id(self):
        return self.get_season_id(self.tmdb_type, self.tmdb_id, self.season)


class Episode(CrewMemberMediaList):
    @cached_property
    def item_id(self):
        return self.get_episode_id(self.tmdb_type, self.tmdb_id, self.season, self.episode)

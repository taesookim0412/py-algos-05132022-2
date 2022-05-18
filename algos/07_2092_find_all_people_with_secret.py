# 43 / 60 (pass)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        # There must be a way to sort by key after instead of before it is grouped.

        meetings.sort(key=lambda x: x[2])
        grps = itertools.groupby(meetings, lambda x: x[2])

        secret_holders = set([0, firstPerson])

        # forward pass
        for meeting_time, meeting_info in grps:
            for meeting in list(meeting_info):
                person_x, person_y, time = meeting
                if person_x in secret_holders or person_y in secret_holders:
                    secret_holders.add(person_x)
                    secret_holders.add(person_y)
            for meeting in reversed(list(meeting_info)):
                person_x, person_y, time = meeting
                if person_x in secret_holders or person_y in secret_holders:
                    secret_holders.add(person_x)
                    secret_holders.add(person_y)
        return secret_holders
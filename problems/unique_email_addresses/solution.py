class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '').split('+')[0]
            output.add('{}@{}'.format(local, domain))
        return len(output)    
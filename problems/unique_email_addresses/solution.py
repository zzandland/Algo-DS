class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s_ = set()
        for email in emails:
            local, domain = email.split('@')
            local = re.sub(r'\+.*', '', local.replace('.', ''))
            s_.add(local + '@' + domain)
        return len(s_)    
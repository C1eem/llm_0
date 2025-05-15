import re
from typing import List

class TechnicalTokenizer:
    def __init__(self):

        self.tech_terms = {
            'RESTful API', 'OAuth2 токен', 'мкд', 'API', 'JSON', 'XML',
            'HTTP', 'HTTPS', 'JWT', 'SSL', 'TLS', 'SOAP', 'GraphQL',
            'микросервис', 'вебхук', 'SDK', 'UI', 'UX', 'CLI', 'SaaS',
            'PaaS', 'IaaS', 'OAuth', 'OpenID', 'SSO', 'CORS', 'CSRF',
            'RPC', 'gRPC', 'WebSocket', 'CDN', 'DNS', 'IP', 'TCP', 'UDP',
            'FTP', 'SSH', 'CI/CD', 'DevOps', 'K8s', 'API Gateway'
        }

        self.patterns = [
            r'(?:GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+[/\w\.\-{}]+',
            r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}',
            r'[0-9a-fA-F]{32,}',
            r'(?:v\d+\.\d+\.\d+|API\s+v\d+)',
            r'[\w\.-]+@[\w\.-]+\.\w+',
            r'(?:https?://)?[\w\.-]+\.\w+(?:/\S*)?',
            r'\d+\s*(?:ms|s|KB|MB|GB|TB)',
            r'[A-Z][a-zA-Z0-9_]*|[a-z][a-zA-Z0-9_]*|[A-Z][A-Z0-9_]+',
            r'\d{4}-\d{2}-\d{2}|\d{2}\.\d{2}\.\d{4}',
            r'\{.*?\}|\[.*?\]',
            r'(?:/?[\w\-\.]+)+/[\w\-\.]+(?:\.\w+)?'
        ]

        self.combined_pattern  = re.compile(
            '|'.join(f'(?:{p})' for p in self.patterns) +
            '|' +
            '|'.join(f'(?:{re.escape(term)})' for term in sorted(self.tech_terms, key=len, reverse=True))
        )

        self.word_pattern = re.compile(r'\w+|[^\w\s]')

    def tokenize(self, text: str) -> List[str]:
        special_tokens = []
        for match in self.combined_pattern.finditer(text):
            special_tokens.append((match.start(), match.end(), match.group()))

        special_tokens.sort()

        tokens = []
        last_pos = 0

        for start, end, token in special_tokens:
            if last_pos < start:
                before = text[last_pos:start]
                tokens.extend(self.word_pattern.findall(before))

            tokens.append(token)
            last_pos = end

        if last_pos < len(text):
            remaining = text[last_pos:]
            tokens.extend(self.word_pattern.findall(remaining))

        return tokens
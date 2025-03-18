class Solution:
    def simplifyPath(self, path: str) -> str:
        components = [component for component in path.split('/') if component]

        stack = []

        for component in components:
            if component == '.':
                pass
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        return '/' + '/'.join(stack)
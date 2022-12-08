# Упражнение 8.13

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('yaroslav', 'kasatkin',
                             location='sofia', field='programming, python',
                             hobby='games')
print(user_profile)

def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
	    # check if there is no user exist to create list for group(groups_per_user value's)
	    # it is to avoid the new group overide the old groups_per_user when adding new group to group's list
            if user not in user_groups:  
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups



print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# output:
# {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}

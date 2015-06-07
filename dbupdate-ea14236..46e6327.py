from Core.db import session
from Core.maps import Group, Access

def addaccess(name, access):
    print "Adding %s" % (name)
    command=Access(name=name)
    session.add(command)
    if access == 2:
        command.groups.append(session.merge(Group.load(id=2)))
        command.groups.append(session.merge(Group.load(id=3)))
        command.groups.append(session.merge(Group.load(id=4)))
    elif access == 3:
        command.groups.append(session.merge(Group.load(id=3)))
        command.groups.append(session.merge(Group.load(id=4)))
    elif access != 1:
        command.groups.append(session.merge(Group.load(id=access)))

print "Setting up new access levels"
addaccess("is_member", 3)
addaccess("arthur_dashboard", 3)

session.commit()
session.close()

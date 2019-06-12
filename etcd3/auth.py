class Auth(object):


    def __init__(self, etcd_client=None):
        self.etcd_client = etcd_client
        
        
    def user_add(self,name):
        user_add = self.etcd_client.useradd(name)
        return user_add

    def user_delete(self, name):
        user_delete = self.etcd_client.userdelete(name)
        return user_delete

    def user_passwd(self, name,password):
        user_passwd = self.etcd_client.userpasswd(name,password)
        return user_passwd

    def user_grandrole(self, name, role):
        user_grandrole = self.etcd_client.usergrandrole(name,role)
        return user_grandrole

    def user_revokerole(self, name, role):
        user_revokerole = self.etcd_client.userrevokerole(name,role)
        return user_revokerole

    def user_get(self,user):
        user_get = self.etcd_client.userget(user)
        for role in user_get.roles:
            yield role

    def user_list(self):
        user_list = self.etcd_client.userlist()
        for user in user_list.users:
            yield user

    def role_add(self,role):
        role_add = self.etcd_client.roleadd(role)
        return role_add

    def role_delete(self,role):
        role_delete = self.etcd_client.roledelete(role)
        return role_delete

    def role_list(self):
        role_list = self.etcd_client.rolelist()

        for role in role_list.roles:
            yield role

    def role_get(self,role):
        role_get = self.etcd_client.roleget(role)
        for key in role_get.perm:
            perm={}
            perm_enum = ['READ','WRITE','READWRITE']
            perm['permTyp,e']=perm_enum[key.permType]
            perm['path']=(key.key).decode('utf-8')
            perm['range_end']=(key.range_end).decode('utf-8')
            yield perm

    def role_grantpermission(self, role, path, perm_type ,prefix):
        role_grantpermission = self.etcd_client.rolegrantpermission(role, path, perm_type ,prefix)
        return role_grantpermission

    def role_revokepermission(self, role, path,prefix):
        role_revokepermission = self.etcd_client.rolerevokepermission(role, path, prefix)
        return role_revokepermission



# this ansible/jinja2 filter plugin allows you to use passlib's *_crypt functions
# until ansible 2.0 comes out - see https://github.com/ansible/ansible/issues/11244.
#
# this filter depends on passlib being installed:
# $ pip install passlib
#
# put this into your playbook's `filter_plugins` folder.
#
# usage example:
# - name: create user
#   user:
#     name: username
#     password: "{{ user_password | passlib_hash('sha512', user_salt) }}"

from ansible import errors

try:
    import passlib
except Exception, e:
    raise errors.AnsibleFilterError('passlib package is not installed')

def passlib_hash(pw, alg = 'sha512', salt = None, rounds = None, implicit_rounds = None, relaxed = None):
    return crypt_method(alg).encrypt(pw, salt = salt, rounds = rounds, implicit_rounds = implicit_rounds, relaxed = relaxed)

def crypt_method(alg):
    return getattr(passlib.hash, alg + '_crypt')

class FilterModule(object):
    def filters(self):
        return {
            'passlib_hash' : passlib_hash
        }

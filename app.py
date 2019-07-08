from bottle import route, run, template, request, response
import json


users = [{"name": "jade"}, {"name": "zoe"}, {"name": "alex"}]
messages = [{"msg": "User added"}, {"msg": "user already exists"}, {"msg": "User not found"}, {"msg": "user deleted successfully"}]


@route('/')
def index():
    return template("index.html")


@route('/api/getUsers', method="GET")
def get_user():
    return json.dumps(users)


@route('/api/addUser', method="POST")
def add_user():
    new_user = request.POST.get("name")

    for thing in users:
        if thing.get("name") != new_user:
            message = messages[1]

        else:users.append({"name": new_user})
            message = messages[0]

    return json.dumps(message)


@route('/api/deleteUser', method="POST")
def delete_user():
    user_to_delete = request.POST.get("name")
    for thing in users:
        print("delete")
        for v in thing:
            print(v)

            if user_to_delete is v:
                print("in deleting function")
                users.remove(thing)
                return json.dumps(messages[3])
            else:
                print("in not deleting")
                return json.dumps(messages[2])


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()


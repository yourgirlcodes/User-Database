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
def add_color():
    new_user = request.POST.get("name").lower()
    for dict_el in users:
        if new_user == dict_el.get("name"):
            return json.dumps(messages[1])
    new_dict_el = {
        "name": new_user
    }
    users.append(new_dict_el)
    return json.dumps(messages[0])


@route('/api/deleteUser', method="POST")
def delete_user():
    delete_this_user = request.POST.get("name").lower()
    for index, value in enumerate(users):
        if value["name"] == delete_this_user:
            del users[index]
            return json.dumps(messages[3])

    return json.dumps(messages[2])


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()


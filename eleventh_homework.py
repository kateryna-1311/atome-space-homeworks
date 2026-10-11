import requests
from rich import print

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users() -> dict:
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    return {"status_code": response.status_code, "data": response.json()}


def get_user(user_id: int) -> dict:
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return {"status_code": response.status_code, "data": response.json()}


def create_user(user_data: dict) -> dict:
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    response.raise_for_status()
    return {"status_code": response.status_code, "data": response.json()}


def modify_user(user_id: int, user_data: dict) -> dict:
    response = requests.patch(f"{BASE_URL}/users/{id}", json=user_data)
    response.raise_for_status()
    return {"status_code": response.status_code, "data": response.json()}


def remove_user(user_id: int) -> dict:
    response = requests.delete(f"{BASE_URL}/users/{id}")
    response.raise_for_status()
    return {"status_code": response.status_code, "data": response.json()}


def show_menu() -> None:
    print("1.Show all users")
    print("2.Show user by ID")
    print("3.Create user")
    print("4.Update user")
    print("5.Delete user")
    print("0.Exit")


def main() -> None:
    print("hello")
    while True:
        show_menu()
        choice = input("What do you want to do? ").strip()

        if choice in ("1", "show all users"):
            _show_all_users()
        elif choice in ("2", "show user by ID"):
            _show_user_by_id()
        elif choice in ("3", "create user"):
            _create_new_user()
        elif choice in ("4", "update user"):
            _update_user_info()
        elif choice in ("5", "delete user"):
            _delete_user_by_id()
        elif choice in ("0", "exit"):
            break


def _show_all_users() -> None:
    try:
        result = get_users()
        print(result)
    except requests.exceptions.HTTPError as error:
        print(
            f"HTTP error (Code {error.response.status_code}): {error.response.reason}"
        )
    except requests.exceptions.RequestException:
        print("Network error")


def _show_user_by_id() -> None:
    user_id = input("Enter user ID: ").strip()
    if not user_id.isdigit():
        print("ID must be a number. Please try again")
        return
    try:
        result = get_user(int(user_id))
        print(result)
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            print(f"User with ID {user_id} not found.")
        else:
            print(f"HTTP error ({error.response.status_code}): {error.response.reason}")
    except requests.exceptions.RequestException:
        print("Network error")


def _create_new_user() -> None:
    new_user = _get_user_form_data()
    try:
        result = create_user(new_user)
        print(result)
    except requests.exceptions.HTTPError as error:
        print(
            f"HTTP error (Code {error.response.status_code}): {error.response.reason}"
        )
    except requests.exceptions.RequestException:
        print("Network error")


def _update_user_info() -> None:
    user_id = input("Enter user ID to update: ").strip()
    if not user_id.isdigit():
        print("ID must be a number.")
        return
    new_name = input("Enter new name (leave empty to skip): ").strip()
    new_email = input("Enter new email (leave empty to skip): ").strip()
    new_data = {}
    if new_name:
        new_data["name"] = new_name
    if new_email:
        new_data["email"] = new_email
    if not new_data:
        print("No fields provided for update.")
        return
    try:
        result = modify_user(int(user_id), new_data)
        print(result)
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            print(f"User with ID {user_id} not found.")
        else:
            print(f"HTTP error: {error}")
    except requests.exceptions.RequestException:
        print("Network error.")


def _delete_user_by_id() -> None:
    user_id = input("Enter user ID to delete: ").strip()
    if not user_id.isdigit():
        print("ID must be a number.")
        return
    try:
        result = remove_user(int(user_id))
        print(result)
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            print(f"User with ID {user_id} not found.")
        else:
            print(f"HTTP error: {error}")
    except requests.exceptions.RequestException:
        print("Network error.")


def _get_user_form_data() -> dict:
    name = input("Enter Name: ").strip()
    username = input("Enter Username: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone: ").strip()
    website = input("Enter Website: ").strip()
    street = input("Enter Street: ").strip()
    suite = input("Enter Suite: ").strip()
    city = input("Enter City: ").strip()
    zipcode = input("Enter Zipcode: ").strip()
    lat = input("Enter Geo Lat: ").strip()
    lng = input("Enter Geo Lng: ").strip()
    company_name = input("Enter Company Name: ").strip()
    catch_phrase = input("Enter Catch Phrase: ").strip()
    bs = input("Enter BS: ").strip()
    return {
        "name": name,
        "username": username,
        "email": email,
        "address": {
            "street": street,
            "suite": suite,
            "city": city,
            "zipcode": zipcode,
            "geo": {"lat": lat, "lng": lng},
        },
        "phone": phone,
        "website": website,
        "company": {
            "name": company_name,
            "catchPhrase": catch_phrase,
            "bs": bs,
        },
    }


main()

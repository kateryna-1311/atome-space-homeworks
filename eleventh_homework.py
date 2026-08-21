import requests
from rich import print

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users() -> dict:
    response = requests.get(BASE_URL + "/users")
    response.raise_for_status()
    result = {"status_code": response.status_code, "data": response.json()}
    return result


def get_user(user_id: int) -> dict:
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    result = {"status_code": response.status_code, "data": response.json()}
    return result


def create_user(user_data: dict) -> dict:
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    response.raise_for_status()
    result = {"status_code": response.status_code, "data": response.json()}
    return result


def modify_user(user_id: int, user_data: dict) -> dict:
    response = requests.patch(f"{BASE_URL}/users/{id}", json=user_data)
    response.raise_for_status()
    result = {"status_code": response.status_code, "data": response.json()}
    return result


def remove_user(user_id: int) -> dict:
    response = requests.delete(f"{BASE_URL}/users/{id}")
    response.raise_for_status()
    result = {"status_code": response.status_code, "data": response.json()}
    return result


def show_menu() -> None:
    print("1.Show all users")
    print("2.Show user by ID")
    print("3.Create user")
    print("4.Update user")
    print("5.Delete user")
    print("0.Exit")


def main() -> None:  # noqa: C901
    print("hello")
    while True:
        show_menu()
        choice = input("What do you want to do?").strip()
        if choice in ("1", "show all users"):
            try:
                result = get_users()
                print(result)
            except requests.exceptions.HTTPError as error:
                print(
                    f"HTTP error (Code {error.response.status_code}): {error.response.reason}"
                )
            except requests.exceptions.RequestException:
                print("Network error")
        elif choice in ("2", "show user by ID"):
            user_id = input("Enter user ID: ")
            if not user_id.isdigit():
                print("ID must be a number. Please try again")
                continue
            user_id = int(user_id)
            try:
                result = get_user(user_id)
                print(result)
            except requests.exceptions.HTTPError as error:
                if error.response.status_code == 404:
                    print(f"User with ID {user_id} not found.")
                else:
                    print(
                        f"HTTP error ({error.response.status_code}): {error.response.reason}"
                    )
            except requests.exceptions.RequestException:
                print("Network error")
        elif choice in ("3", "create user"):
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
            new_user = {
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
            try:
                result = create_user(new_user)
                print(result)
            except requests.exceptions.HTTPError as error:
                print(
                    f"HTTP error (Code {error.response.status_code}): {error.response.reason}"
                )
            except requests.exceptions.RequestException:
                print("Network error")
        elif choice in ("4", "update user"):
            user_id = input("Enter user ID to update: ").strip()
            if not user_id.isdigit():
                print("ID must be a number.")
                continue
            new_name = input("Enter new name (leave empty to skip): ").strip()
            new_email = input("Enter new email (leave empty to skip): ").strip()

            new_data = {}
            if new_name:
                new_data["name"] = new_name
            if new_email:
                new_data["email"] = new_email

            if not new_data:
                print("No fields provided for update.")
                continue
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
        elif choice in ("5", "delete user"):
            user_id = input("Enter user ID to delete: ").strip()
            if not user_id.isdigit():
                print("ID must be a number.")
                continue
            try:
                result = remove_user(user_id)
                print(result)
            except requests.exceptions.HTTPError as error:
                if error.response.status_code == 404:
                    print(f"User with ID {user_id} not found.")
                else:
                    print(f"HTTP error: {error}")
            except requests.exceptions.RequestException:
                print("Network error.")
        elif choice in ("0", "exit"):
            break


main()

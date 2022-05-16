import http from "@/../http-common";

class UserService {
    getUsers() {
        return http.get("/users");
    }

    getUser(token) {
        return http.get('/user_by_token', {
            params:
                {token: token},
        });
    }

    updateUser(token, user) {
        return http.put('/user_by_token/',
                {token: token,
                first_name: user.first_name,
                last_name: user.last_name,
                email: user.email},
        );
    }

    login(username, password) {
        return http.post("auth/", {
            username: username, password: password
        });
    }
}

export default new UserService();

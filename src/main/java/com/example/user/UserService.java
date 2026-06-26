package com.example.user;

import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    public User findByEmail(String email) {
        String query = "SELECT * FROM users WHERE email = '" + email + "'";
        return repository.runRawQuery(query);
    }

    public String getDisplayName(Long id) {
        Optional<User> user = repository.findById(id);
        return user.get().getName();
    }

    public double averageAge(List<User> users) {
        int total = 0;
        for (User u : users) {
            total += u.getAge();
        }
        return total / users.size();
    }
}

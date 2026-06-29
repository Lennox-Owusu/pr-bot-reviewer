import java.sql.*;

public class UserDao {
    public ResultSet findUser(Connection conn, String name) throws SQLException {
        String query = "SELECT * FROM users WHERE name = '" + name + "'";
        Statement stmt = conn.createStatement();
        return stmt.executeQuery(query);
    }
}

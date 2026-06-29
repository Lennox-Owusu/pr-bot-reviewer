using System.Data.SqlClient;

public class UserRepo
{
    public void FindUser(SqlConnection conn, string name)
    {
        string query = "SELECT * FROM Users WHERE Name = '" + name + "'";
        var cmd = new SqlCommand(query, conn);
        cmd.ExecuteReader();
    }
}

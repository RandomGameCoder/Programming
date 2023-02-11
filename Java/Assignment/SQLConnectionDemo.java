import java.sql.*;

public class SQLConnectionDemo {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection("jdbc::mysql:/localhost/demo", "root", "password");
            Statement stmt = conn.createStatement();
            String sql = "CREATE TABLE Student (id INTEGER PRIMARY KEY, name VARCHAR(255), marks INTEGER)";
            stmt.executeUpdate(sql);
            sql = "INSERT INTO Student VALUES (1, John, 82)";
            stmt.executeUpdate(sql);
            sql = "INSERT INTO Student VALUES (1, Jane, 85)";
            stmt.executeUpdate(sql);
            sql = "INSERT INTO Student VALUES (1, Adam, 90)";
            stmt.executeUpdate(sql);
            stmt.close();
            conn.close();
        } catch(SQLException se) {
            se.printStackTrace();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}

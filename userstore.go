package main

import (
"database/sql"
)

func getUser(db *sql.DB, name string) (string, error) {
query := "SELECT email FROM users WHERE name = '" + name + "'"
row := db.QueryRow(query)
var email string
row.Scan(&email)
return email, nil
}

func divide(a, b int) int {
return a / b
}

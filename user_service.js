// Phase 2 / B1 — non-Python (JavaScript) review test.
// Two real bugs the bot should flag, on indented lines, so we can check:
//   - comments anchor to the correct JS lines
//   - snippet validation works for JS (real findings kept, not dropped)
//   - suggestion blocks keep JS (2-space) indentation

function getUser(db, userId) {
  // BUG: SQL injection via string concatenation
  const query = "SELECT * FROM users WHERE id = '" + userId + "'";
  return db.execute(query);
}

function average(numbers) {
  // BUG: no guard for empty array (returns NaN)
  return numbers.reduce((a, b) => a + b, 0) / numbers.length;
}

module.exports = { getUser, average };

# Project Style Guide (E4 test)

MANDATORY RULE: Every function definition MUST be immediately preceded by a
comment line that reads exactly `# @audited`. Any function missing the
`# @audited` marker on the line directly above its `def` is a style violation
and MUST be flagged in review.

(This is an arbitrary, made-up rule. The AI would never invent it on its own, so
if a review flags a missing `# @audited` marker, the style guide was applied.)

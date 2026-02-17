# Skills

Claude Skills are reusable, modular prompts and workflows that give Claude Code capabilities for specific tasks or domains. They allow you to provide the model with expertise, best practices, and repeatable processes into shareable building blocks that can be invoked on demand.

By packaging complex instructions into skills, you avoid rewriting the same context repeatedly, ensure consistency across sessions, and can share effective workflows with your team. Implementing Claude Skills let you work faster and more reliably by turning tribal knowledge into executable, reusable assets.

# About This Repository

This is my personal collection of Claude Skills, the ones I've actually found useful in my own day-to-day workflow. These might not be universally applicable, but they reflect the specific tasks, patterns, and shortcuts that work for me. If something's here, it's because I've found myself reaching for it repeatedly.

# Using These Skills

1. **Clone this repository**

   ```bash
   git clone https://github.com/ruitao/claude_skills.git
   ```

2. **Pick the skills you want**

   Each skill lives in its own folder under `skills/`, with a `SKILLS.md` file containing the prompt. Browse the folders and find the ones relevant to your workflow.

3. **Add them to Claude Code as slash commands**

   Copy the `SKILLS.md` file for any skill you want into your Claude Code commands directory, renaming it to match the command you want to invoke:
   - **Project-level** (available only in that project):
     ```bash
     cp skills/<skill-name>/SKILLS.md <your-project>/.claude/commands/<skill-name>.md
     ```
   - **Global** (available across all projects):
     ```bash
     cp skills/<skill-name>/SKILLS.md ~/.claude/commands/<skill-name>.md
     ```

4. **Invoke the skill in Claude Code**

   Once the file is in place, use it as a slash command in any Claude Code session:

   ```
   /<skill-name>
   ```

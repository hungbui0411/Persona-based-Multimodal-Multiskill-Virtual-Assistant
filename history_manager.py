class HistoryManager:
    def __init__(self, prior_history=None, max_kept=11, persona_specs=None):
        if prior_history is None:
            prior_history = [
                {"role": "system", "content": "You are a helpful assistant."},
            ]
        self.history_logs = prior_history
        self.max_kept = max_kept
        self.persona_specs = persona_specs
        self.log_file_name = f"data/history_logs/{self.persona_specs.name}_history.txt"
        with open(self.log_file_name, 'w') as writer:
            writer.write("===Persona Specifications===\n")
            writer.write(f"Name: {self.persona_specs.name}\n")
            writer.write(f"Greeting: {self.persona_specs.greeting}\n")
            writer.write(f"Short description: {self.persona_specs.short_description}\n")
            writer.write(f"Long description: {self.persona_specs.long_description}\n")
            writer.write(f"Character categories: {self.persona_specs.character_categories}\n")
            writer.write(f"Persona definition: {self.persona_specs.persona_definition}\n")
            writer.write(f"User name: {self.persona_specs.user_name}\n")
            writer.write("===Start of Conversation Logs===")


    def external_write(self, message):
        with open(self.log_file_name, 'a') as writer:
            writer.write(f"{message}\n")

    def write_to_log(self, role, message, scene_transition=False):
        if scene_transition:
            with open(self.log_file_name, 'a') as writer:
                writer.write(f"{message}\n")
            return

        if role == "user":
            role = self.persona_specs.user_name
        else:
            role = self.persona_specs.name
        with open(self.log_file_name, 'a') as writer:
            writer.write(f"{role}: {message}\n")

        return

    def update_history(self, role, message, scene_transition=False):
        if scene_transition:
            self.write_to_log(role, message, scene_transition=True)
            log = {}
        log = {
            "role": role,
            "content": message
        }
        # Write the discourse turn in a separate log file
        self.write_to_log(role, message)
        # Append history log so the persona knows which history to use for conversational purposes
        self.history_logs.append(log)
        # Update the max kept number of conversational turns
        if len(self.history_logs) > self.max_kept:
            self.history_logs.pop(1) # We do not want to pop the system message. We only want to interact with the assistant and the user

class Solution:
    def process_preferences(preference_data):
        result = {}

        for prompt_id, response_A, response_B in preference_data:
            if preference == 'A':
                chosen_response = response_A
                rejected_response = response_B
            elif preference == 'B':
                chosen_response = response_B
                rejected_response = response_A
            else:
                raise ValueError("Preference must be 'A' or 'B'")
            
            if prompt_id not in result:
                result[prompt_id].append((chosen_response, rejected_response))
            
        return result
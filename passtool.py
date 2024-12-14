import re

# Function to check the password strength
def check_password_strength(password):
    feedback = []
    strength_score = 0

    # 1. Check for length (minimum 8 characters)
    if len(password) < 8:
        feedback.append("⚠️ Password is too short! (minimum length is 8 characters).")
    else:
        feedback.append("✅ Password length is good.")
        strength_score += 1

    # 2. Check for uppercase letter
    if re.search(r'[A-Z]', password):
        feedback.append("✅ Uppercase letter is present.")
        strength_score += 1
    else:
        feedback.append("⚠️ No uppercase letter found. Consider adding one.")

    # 3. Check for lowercase letter
    if re.search(r'[a-z]', password):
        feedback.append("✅ Lowercase letter is present.")
        strength_score += 1
    else:
        feedback.append("⚠️ No lowercase letter found. Consider adding one.")

    # 4. Check for numbers
    if re.search(r'[0-9]', password):
        feedback.append("✅ Number is present.")
        strength_score += 1
    else:
        feedback.append("⚠️ No number found. Consider adding one.")

    # 5. Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("✅ Special character is present.")
        strength_score += 1
    else:
        feedback.append("⚠️ No special character found. Consider adding one.")

    # Suggest improvements based on score
    if strength_score < 4:
        feedback.append("❗ Suggestion: Your password is weak. Please add more complexity (uppercase, lowercase, numbers, and special characters).")
    elif strength_score < 5:
        feedback.append("⚡ Suggestion: Your password is decent. Add a little more variety (like special characters or more length).")
    else:
        feedback.append("🎉 Your password is strong!")

    # Convert strength score into a user-friendly strength rating
    final_strength = get_password_strength(strength_score)
    feedback.append(f"\n🔒 Final Password Strength: {final_strength}")

    return feedback

# Convert strength score into a user-friendly strength rating
def get_password_strength(score):
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Function to display the logo and introduction
def display_logo():
    print("""
██████╗  █████╗ ███████╗███████╗███████╗ ██████╗ ███████╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██████╔╝███████║███████╗███████╗███████╗██████╔╝███████╗   ██║
██╔═══╝ ██╔══██║╚════██║╚════██║╚════██║██╔══██╗╚════██║   ██║
██║     ██║  ██║███████║███████║███████║██║  ██║███████║   ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝
    """)
    print("\nWelcome to the Password Complexity Checker!\n")
    print("Let's check how strong your password is and help you make it even stronger!")
    print("-----------------------SAKIB SHAIKH------------------------------------")

# Main function to interact with the user
def main():
    display_logo()

    while True:
        # Get password input from the user
        password = input("\nPlease enter a password to check its strength: ").strip()

        print("\n🔍 Analyzing your password...\n")
        
        # Check the strength of the password
        feedback = check_password_strength(password)
        
        # Display the feedback
        for item in feedback:
            print(f"   {item}")

        print("\n-----------------------------------------------------------")
        
        # Ask if the user wants to check another password
        retry = input("\nWould you like to check another password? (yes/no): ").strip().lower()
        if retry == 'no':
            print("\nThank you for using the Password Complexity Checker! Stay secure! 🔐")
            break
        elif retry != 'yes':
            print("\nPlease enter 'yes' or 'no'.")

# Run the program
if __name__ == "__main__":
    main()

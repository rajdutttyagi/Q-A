# from llm import answer_user_query

# if __name__ == "__main__":
#     # User se input lena
#     user_query = input("👤 Enter your query: ")

#     # Answer generate karwana
#     answer = answer_user_query(user_query)

#     # Result display
#     print("\n🤖 Answer:\n", answer)
from up_retriver_LLM import answer_user_query

if __name__ == "__main__":
    user_query = input("Enter something: ")
    #user_query = "hello"

    # print(f"You entered: {user_query}")

    answer = answer_user_query(user_query)
    print("\n Answer:\n", answer)

#What is mentioned about Amazon's revenue?

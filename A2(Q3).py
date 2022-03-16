college = { "Student":input("enter the name: "),
"SRN":input("enter the SRN: ")}
college.update({"Section":input("enter the Section: "),"phone":input("enter the Phone number: ")})
print(college)
college.update({"Room number":input("enter the updated room number: ")})
print(college)

import demoji



# Now use demoji to find emojis in the text
text = '''
 "Just deployed a 🤖 powered by ☁️ with zero bugs 🐞... until the toaster 🔌 
tried to connect to the blockchain 🧱. Now my coffee maker ☕ is mining crypto 💰.
 #TechLife  😂💻🔥"
'''
found_emojis = demoji.findall(text)
print(found_emojis)

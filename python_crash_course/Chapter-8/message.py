# Упражнения 8.9 - 8.11

messages = ['hello', 'goodbye', 'how are you']
sent_messages = []


def send_messages(msg, send_msg):
    while msg:
        message = msg.pop()
        print(message)
        send_msg.append(message)


def show_messages(msg):
    for message in msg:
        print(message.title())


send_messages(messages[:], sent_messages)
show_messages(messages)

print(messages)
print(sent_messages)

class ContactPhoto(ILeftBody, AsyncImage):
    pass

class MessageButton(IRightBodyTouch, MaterialIconButton):
    phone_number = StringProperty()

    def on_release(self):
        # sample code:
        Dialer.send_sms(phone_number, "Hey! What's up?")
        pass

# Sets up ScrollView with MaterialList, as normally used in Android:
sv = ScrollView()
ml = MaterialList()
sv.add_widget(ml)

contacts = [
    ["Annie", "555-24235", "http://myphotos.com/annie.png"],
    ["Bob", "555-15423", "http://myphotos.com/bob.png"],
    ["Claire", "555-66098", "http://myphotos.com/claire.png"]
]

for c in contacts:
    item = TwoLineAvatarIconListItem(
        text=c[0],
        secondary_text=c[1]
    )
    item.add_widget(ContactPhoto(source=c[2]))
    item.add_widget(MessageButton(phone_number=c[1])
    ml.add_widget(item)
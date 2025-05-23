import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print("----PERSON----")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute("id")))
    # person.getElementsByTagName("name") -> [<Element name>] (A list containing one XML element node: <name>Alice</name>)
    # person.getElementsByTagName("name")[0] -> <Element name> (<name>Alice</name>)
    # person.getElementsByTagName("name")[0].childNodes[0] -> <Text node: "Alice">
    # person.getElementsByTagName("name")[0].childNodes[0].data -> "Alice"
    print("Name: {}".format(person.getElementsByTagName("name")[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName("age")[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName("weight")[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName("height")[0].childNodes[0].data))

# how to edit existing xml file
persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
persons[0].setAttribute("id", '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"

domtree.writexml(open("data2.xml", "w"))

# how to add new elements to the xml file
newperson = domtree.createElement('person')
newperson.setAttribute("id", "6")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Paul Green"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("19"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("80"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("179"))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open("data3.xml", "w"))


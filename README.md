# Flask-Marshmallow-SQLAlchemy 

## What is the Serialization?

In computer science, in the context of data storage, serialization is the process 
of translating data structures or object state into a format that can be stored 
(for example, in a file or memory buffer) or transmitted (for example, across
a network connection link) and reconstructed later (possibly in a different computer environment).
When the resulting series of bits is reread according to the serialization format,
it can be used to create a semantically identical clone of the original object.
For many complex objects, such as those that make extensive use of references,
this process is not straightforward. Serialization of object-oriented objects
does not include any of their associated methods with which they were previously
linked.


## Serialization formats:

* XML was used to produce a human readable text-based encoding. Such an encoding can be useful for persistent objects that may be read and understood by humans, or communicated to other systems regardless of programming language. It has the disadvantage of losing the more compact, byte-stream-based encoding, but by this point larger storage and transmission capacities made file size less of a concern than in the early days of computing. Binary XML had been proposed as a compromise which was not readable by plain-text editors, but was more compact than regular XML. In the 2000s, XML was often used for asynchronous transfer of structured data between client and server in Ajax web applications.

* JSON is a lighter plain-text alternative to XML which is also commonly used for client-server communication in web applications. JSON is based on JavaScript syntax, but is supported in other programming languages as well.

* YAML, is similar to JSON and includes features that make it more powerful for serialization, more "human friendly," and potentially more compact. These features include a notion of tagging data types, support for non-hierarchical data structures, the option to structure data with indentation, and multiple forms of scalar data quoting.

## Short conclusion:

Serialization is a technique for describing a data structure with information about the structure itself embedded in the data. JSON is a lightweight type of serialization, e.g., ```{prop:{prop:1}}```. Transfer that to another computer and minimally you can then work with that object's properties with the same basic relationship of ```prop.prop```


<a href="https://ibb.co/eDaAbx"><img width="100%"  src="https://preview.ibb.co/mHy7Oc/diagram.png" alt="diagram" border="0"></a>


## Schema.org is god, remember

This project uses schema.org as the main resource for the standardization of data types in a schema

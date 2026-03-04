from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()


##schema
class Review(TypedDict):
    summary: str
    sentiment: str


struct_model=model.with_structured_output(Review)

result=struct_model.invoke(''' I've lost count of the number of times I have seen this movie, but it is more than 20. It has to be one of the best movies ever made. It made me take notice Morgan Freeman and Tim Robbins like I had never noticed any actors before.

I have from a very young age been a huge fan of anything Stephen King writes and had already read the short story that this movie is based on years prior to seeing this movie.

Not everything Stephen King has written that gets turned into a movie comes out well, but this is as close to perfection as it gets and has everything you could ever want in a movie.

Something that is outstanding is the fact that it has no real action, no special effects and no gimmicks. 99% of the movie is just men in a prison uniforms talking. Yet it absolutely hooks you almost from the beginning and has you glued to the screen to the end.

For me what really makes this film one of the best is the message of eternal hope it conveys throughout. The never ever give up hope attitude of the main character so well conveyed by Tim Robbins. The ending is just spine tingling every time I see it, no matter how many times I have seen it.

Brilliant, brilliant movie and a must see for everyone.
''')
print(result)
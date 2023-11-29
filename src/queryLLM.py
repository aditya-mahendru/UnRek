from langchain.llms import Ollama

# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory

MODEL = "openhermes2.5-mistral:7b-fp16"

llm = Ollama(base_url="http://localhost:11434", model=MODEL, temperature=0.1)


def singleQuestionForInfo(property, intendedTowards, isBool):
    boolQuery = "This is a yes or no question." if isBool else ""
    query = "Generate a formal worded question intended towards {} asking their {} in their bachelor's prgram.{} Generate without any greetings. Ask for single word answers. Only generate One question".format(
        intendedTowards, property, boolQuery
    )
    return llm(query)


def singleQuestionForPreference(property, isBool):
    query = (
        "Generate a formal worded question asking user their preferred {} for their masters program. Only generate the question expecting a one word answer Only generate One question".format(
            property
        )
        if not isBool
        else "Generate a formal worded question to ask if {} is an immportant factor while looking a masters program.Only generate the question expecting a yes or no answer Only generate One question".format(
            property
        )
    )

    return llm(query)


def searchQuery(property, preference):
    query = "Generate a search prompt to be used in a web search to get University data for a aspiring masters student with {} requirement and the {} preferences. Only generate one result. Do not generate anything besides the query.".format(
        property, preference
    )
    return llm(query)


def summarizeRanking(textContent, property):
    query = "Consider the following University related data from a webpage:{} From the above data generate a list of top 5 universities matching the {} criteria. Only output the rankings along with the critera for your descision.Only use the provided data.Only generate a list of universities".format(
        textContent, property
    )
    # print(llm(query))

    return llm(query)


def genJsonRankings(textContent, property):
    query = r"""{} 
    Convert it to a JSON list of only university names and {} requirement. Just generate the JSON without saying anything and without markdown. Every Json element should be of the following format:
    {{"University":University Name here,{}:Citeria in one word}}
    """.format(
        textContent, property, property
    )

    # print(query)
    # return True
    return llm(query)

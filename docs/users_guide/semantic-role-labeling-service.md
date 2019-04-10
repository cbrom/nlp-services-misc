![singnetlogo](../assets/singnet-logo.jpg?raw=true 'SingularityNET')

# Semantic Role Labeling Service
## Service User's Guide

### Welcome

This service provides a wrapper around [allenlp](https://demo.allennlp.org/semantic-role-labeling)'s great demo and models available for semantic role labeling

[Semantic Role Labeling (SRL)](https://en.wikipedia.org/wiki/Semantic_role_labeling) recovers the latent predicate argument structure of a sentence, providing representations that answer basic questions about sentence meaning, including “who” did “what” to “whom,” etc.


### Using the service on the platform
- The input to the system is straight forward. It is a sentence or group of sentences as defined by the following proto. 
```proto
message InputSentence {
    string sentence = 1;
}
```

- The response to the given query is the references and the tokenized words list defined as:
```proto
message Input {
    string document = 1;
}

message Verbs {
    string verb = 7;
    string description = 8;
    Words tags = 9;
}

message Words {
    repeated string word = 6;
}

message Output{
    repeated Verbs verbs = 10;
    Words words = 11;
}

service SRL {
    rpc resolve (Input) returns (Output) {}
}
```

## Result Interpretation
The result can be interpreted using [PropBank Annotation](https://en.wikipedia.org/wiki/PropBank)

O is usually ignored

ARG-0 is usually PROTO-AGENT

ARG-1 is usually PROTO-PATIENT

ARG-2 is usually benefactive, instrument, attribute

ARG-3 is usually start point, benefactive, instrument, attribute

ARG-4 is usually end point (e.g., for move or push style verbs)

For a given sentence, the list of words and verbs along side their description and tags are returned. Tags are the PropBank tagged labels of each word for a given verb.

The following is the response to the query: "The keys, which were needed to access the building, were locked in the car."
```text
verbs {
  verb: "were"
  description: "The keys , which [V: were] needed to access the building , were locked in the car ."
  tags {
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "B-V"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
  }
}
verbs {
  verb: "needed"
  description: "[ARG1: The keys] , [R-ARG1: which] were [V: needed] [ARGM-PRP: to access the building] , were locked in the car ."
  tags {
    word: "B-ARG1"
    word: "I-ARG1"
    word: "O"
    word: "B-R-ARG1"
    word: "O"
    word: "B-V"
    word: "B-ARGM-PRP"
    word: "I-ARGM-PRP"
    word: "I-ARGM-PRP"
    word: "I-ARGM-PRP"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
  }
}
verbs {
  verb: "access"
  description: "The keys , which were needed to [V: access] [ARG1: the building] , were locked in the car ."
  tags {
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "B-V"
    word: "B-ARG1"
    word: "I-ARG1"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
  }
}
verbs {
  verb: "were"
  description: "The keys , which were needed to access the building , [V: were] locked in the car ."
  tags {
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "B-V"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
    word: "O"
  }
}
verbs {
  verb: "locked"
  description: "[ARG1: The keys , which were needed to access the building] , were [V: locked] [ARGM-LOC: in the car] ."
  tags {
    word: "B-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "I-ARG1"
    word: "O"
    word: "O"
    word: "B-V"
    word: "B-ARGM-LOC"
    word: "I-ARGM-LOC"
    word: "I-ARGM-LOC"
    word: "O"
  }
}
words {
  word: "The"
  word: "keys"
  word: ","
  word: "which"
  word: "were"
  word: "needed"
  word: "to"
  word: "access"
  word: "the"
  word: "building"
  word: ","
  word: "were"
  word: "locked"
  word: "in"
  word: "the"
  word: "car"
  word: "."
}

```

A dictionary represenation of this by passing to google.protobuf's message to dictionary gives:
```python
{"verbs": 
    [
        {"verb": "were",
            "description": "The keys , which [V: were] needed to access the building , were locked in the car .",
            "tags": { "word": ["O","O","O","O","B-V","O","O","O","O","O","O","O","O","O","O","O","O"]}
        },
        {"verb": "needed",
            "description": "[ARG1: The keys] , [R-ARG1: which] were [V: needed] [ARGM-PRP: to access the building] , were locked in the car .",
            "tags": { "word": ["B-ARG1","I-ARG1","O","B-R-ARG1","O","B-V","B-ARGM-PRP","I-ARGM-PRP","I-ARGM-PRP","I-ARGM-PRP","O","O","O","O","O","O","O"]}
        },
        {"verb": "access",
            "description": "The keys , which were needed to [V: access] [ARG1: the building] , were locked in the car .",
            "tags": { "word": ["O","O","O","O","O","O","O","B-V","B-ARG1","I-ARG1","O","O","O","O","O","O","O"]}},
        {"verb": "were",
            "description": "The keys , which were needed to access the building , [V: were] locked in the car .",
            "tags": { "word": ["O","O","O","O","O","O","O","O","O","O","O","B-V","O","O","O","O","O"]}},
        {"verb": "locked",
            "description": "[ARG1: The keys , which were needed to access the building] , were [V: locked] [ARGM-LOC: in the car] .",
            "tags": { "word": ["B-ARG1","I-ARG1","I-ARG1","I-ARG1","I-ARG1","I-ARG1","I-ARG1","I-ARG1","I-ARG1","I-ARG1","O","O","B-V","B-ARGM-LOC","I-ARGM-LOC","I-ARGM-LOC","O"]}}
    ],
    "words":{"word": ["The", "keys", ",", "which", "were", "needed", "to", "access", "the", "building", ",", "were", "locked", "in", "the", "car", "."]}
}
        
```


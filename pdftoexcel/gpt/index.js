import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: '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'
});

// console.log(openai);

const chatCompletion = await openai.chat.completions.create({
    model: "gpt-3.5-turbo-16k-0613",
    messages: [{"role": "user", "content": "Hello!"}],
  });
  console.log(chatCompletion.choices[0].message);
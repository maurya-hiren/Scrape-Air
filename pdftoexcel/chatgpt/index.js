// const { Configuration, OpenAIApi } = require("openai");
import { Configuration, OpenAIApi } from 'openai';
// import OpenAI from "openai";
const configuration = new Configuration({
  apiKey: process.env.OPENAI_SECRET_KEY,
});
const openai = new OpenAIApi(configuration);

async function main() {
  const completion = await openai.createChatCompletion({
    model: "gpt-4",
    messages: [{ role: "user", content: "Hello world" }],
  });
  console.log(completion.data.choices[0].message);
}

main();

import React, { useState } from "react";
import { OpenAI } from "openai";
import rawPrompt from "../src/prompt.txt";

function Chatbot() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const apiKey = import.meta.env.VITE_API_KEY;
  const openai = new OpenAI({ apiKey: apiKey, dangerouslyAllowBrowser: true });

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (input.length === 0) {
      return;
    }

    try {
      setMessages((prevMessages) => [
        ...prevMessages,
        { content: input, sender: "user" },
      ]);

      const userInputPrompt = input;
      // Replace with the path to your text file
      await readTextFileAndUseAsPrompt(userInputPrompt);

      setInput("");
    } catch (error) {
      console.error("An error occurred:", error.message);
    }
  };
  const readTextFileAndUseAsPrompt = async (userInputPrompt) => {
    try {
      // Fetch the file content using fetch API
      const response = await fetch(rawPrompt); // Assuming the file is in the same location as Chatbot.jsx
      if (!response.ok) {
        throw new Error(
          `Failed to fetch file prompt.txt: ${response.statusText}`
        );
      }
      const fileContent = await response.text();

      // Append user input prompt to the file content
      const prompt = `${fileContent}\n${userInputPrompt}`;

      // Call the OpenAI API with the prompt
      const aiResponse = await openai.chat.completions.create({
        model: "gpt-4",
        messages: [{ role: "user", content: prompt }],
      });

      // Update messages state with the AI response
      aiResponse.choices.forEach((messageResponse) => {
        setMessages((prevMessages) => [
          ...prevMessages,
          { content: messageResponse.message.content, sender: "bot" },
        ]);
      });
    } catch (error) {
      console.error("Error reading or using the file content:", error);
    }
  };

  const renderFormattedText = (text) => {
    return text.split("\n").map((line, index) => (
      <p key={index} className="mb-1">
        {line}
      </p>
    ));
  };

  return (
    <div className="bg-pink-100 max-h-screen flex flex-col w-4/5 rounded-lg my-6">
      <h1 className="text-6xl text-center font-bold mb-4">Chat with EVITA</h1>
      <div className="flex-1 overflow-y-auto px-4 py-8">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`mb-4 ${
              message.sender === "user"
                ? "flex justify-end"
                : "flex justify-start"
            } `}
          >
            <div
              className={`max-w-md rounded-lg px-4 py-2 shadow-md ${
                message.sender === "user"
                  ? "bg-purple-400 text-white self-end"
                  : "bg-white text-black self-start"
              }`}
            >
              <p className="text-xs font-bold mb-1">
                {message.sender === "user" ? "You" : "Evita"}
              </p>
              {renderFormattedText(message.content)}
            </div>
          </div>
        ))}
      </div>
      <form
        className="flex items-center px-4 py-2 my-6"
        onSubmit={handleSubmit}
      >
        <input
          type="text"
          className="flex-1 border border-gray-300 rounded-lg py-2 px-4 mr-4 focus:outline-none focus:border-blue-500 shadow-md"
          placeholder="Type your message..."
          value={input}
          onChange={handleInputChange}
        />
        <button
          type="submit"
          className="bg-purple-400 text-white px-4 py-2 rounded-lg hover:bg-purple-600 shadow-md outline-none"
        >
          Send
        </button>
      </form>
    </div>
  );
}

export default Chatbot;

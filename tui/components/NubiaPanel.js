import React, { useState } from 'react';
import { Box, Text, TextInput } from 'ink';
export default function NubiaPanel() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');
  const handleSubmit = async () => {
    if (!query.trim()) return;
    try {
      const res = await fetch('http://localhost:5000/nubia/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: query })
      });
      const data = await res.json();
      setAnswer(data.answer || 'No response.');
    } catch(e) {
      setAnswer('Error contacting Nubia.');
    }
    setQuery('');
  };
  return (
    <Box flexDirection="column">
      <Text bold color="#c77dff">🟣 Nubia the Wise</Text>
      <Box marginY={1}>
        <Text>Query: </Text>
        <TextInput value={query} onChange={setQuery} onSubmit={handleSubmit} />
      </Box>
      {answer && <Box borderStyle="single" borderColor="#c77dff44" padding={1}><Text>{answer}</Text></Box>}
    </Box>
  );
}

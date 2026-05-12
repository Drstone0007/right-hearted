import React, { useState } from 'react';
import { Box, Text, useInput } from 'ink';
import ManusPanel from './components/ManusPanel.js';
import NubiaPanel from './components/NubiaPanel.js';
import Dashboard from './components/Dashboard.js';

const TABS = ['📊 Stats', '🔧 Manus', '🟣 Nubia'];

export default function App() {
  const [activeTab, setActiveTab] = useState(0);

  useInput((input, key) => {
    if (key.leftArrow) setActiveTab(prev => Math.max(0, prev - 1));
    if (key.rightArrow) setActiveTab(prev => Math.min(TABS.length - 1, prev + 1));
  });

  return (
    <Box flexDirection="column" padding={1}>
      <Box borderStyle="double" borderColor="#ffffff22" backgroundColor="#ffffff08" padding={1} marginBottom={1}>
        <Text bold color="#00ffff">🐐 Right-Hearted TUI</Text>
      </Box>
      <Box marginBottom={1}>
        {TABS.map((tab, i) => (
          <Box key={tab} paddingX={1}>
            <Text
              bold={i === activeTab}
              underline={i === activeTab}
              backgroundColor={i === activeTab ? '#00ffff22' : undefined}
              color={i === activeTab ? '#00ffff' : '#aaaaaa'}
            >{tab}</Text>
          </Box>
        ))}
      </Box>
      <Box flexDirection="column">
        {activeTab === 0 && <Dashboard />}
        {activeTab === 1 && <ManusPanel />}
        {activeTab === 2 && <NubiaPanel />}
      </Box>
      <Box marginTop={1}><Text color="#666">← → navigate | q quit</Text></Box>
    </Box>
  );
}

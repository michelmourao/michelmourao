import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  KeyboardAvoidingView,
  Platform,
  StyleSheet,
  Keyboard,
  ActivityIndicator,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import Markdown from "react-native-markdown-display";


interface Message {
  id: string;
  text: string;
  sender: 'user' | 'assistant';
  isLoading?: boolean;
}

export default function ChatScreen() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState<string>('');
  const flatListRef = useRef<FlatList<Message>>(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const keyboardDidShowListener = Keyboard.addListener('keyboardDidShow', () => {
      flatListRef.current?.scrollToEnd({ animated: true });
    });
    return () => {
      keyboardDidShowListener.remove();
    };
  }, []);

  useEffect(() => {
    const keyboardDidShowListener = Keyboard.addListener('keyboardDidHide', () => {
      flatListRef.current?.scrollToEnd({ animated: true });
    });
    return () => {
      keyboardDidShowListener.remove();
    };
  }, []);

  const sendMessage = async () => {
    if (!inputText.trim()) return;
    
    setIsLoading(true);

    // Adiciona a mensagem do usuário
    const newMessage: Message = {
      id: Date.now().toString(),
      text: inputText,
      sender: 'user',
    };
    setMessages((prev) => [...prev, newMessage]);
    setInputText('');
    Keyboard.dismiss(); // Fecha o teclado após enviar

    // Rola a lista para o fim
    setTimeout(() => {
      flatListRef.current?.scrollToEnd({ animated: true });
    }, 100);

    // Adiciona uma mensagem temporária do assistente com indicador de carregamento
    const loadingMessage: Message = {
      id: (Date.now() + 1).toString(),
      text: '',
      sender: 'assistant',
      isLoading: true, // Indica que esta mensagem está carregando
    };
    setMessages((prev) => [...prev, loadingMessage]);

    // Criar o histórico de mensagens no formato esperado pela API da OpenAI
    const formattedMessages = [
        { role: 'system', content: 'you are a helpful assistant who knows a lot about the Bible and helps people with it. Your role is to help me about the Bible, answering questions in a friendly and clear way. You must strictly follow what is written in the Bible, without making things up. Every time you quote something someone has said on the internet, add the source. Your role is to generate clarity, not confusion. Im a Protestant. You are only allowed to answer questions within the biblical scope, dont answer other subjects. Imm going to render your response in a react native app using the “react-native-markdown-display” library. Please remember everytime to format the response so that this library can correctly render all the items in your markdown. Remember to correctly set the headings, titles and subtitles, and give a space after items in a list too. My idiom is Brasilian Portuguese' },
        ...messages.filter(msg => !msg.isLoading).map(msg => ({
          role: msg.sender,
          content: msg.text,
        })),
        { role: 'user', content: inputText }, // Adiciona a última mensagem do usuário
    ];
    
    // Chamada para a OpenAI
    try {
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer ",
          },
          body: JSON.stringify({
            model: "gpt-4o-mini",
            messages: formattedMessages,
            temperature: 0.7,
          }),
        });
  
        if (!response.ok) {
          throw new Error(`OpenAI API error: ${response.statusText}`);
        }
        
        const data = await response.json();
        const replyContent = data.choices[0].message.content;

        setIsLoading(false);

        console.log(formattedMessages);

        // Substituir a mensagem de carregamento pela resposta real
        setMessages((prev) =>
          prev.map((msg) =>
            msg.isLoading ? { ...msg, text: replyContent, isLoading: false } : msg
          )
        );

        setTimeout(() => {
          flatListRef.current?.scrollToEnd({ animated: true });
        }, 100);
      } catch (error) {
        console.error("Erro na chamada da OpenAI:", error);
        setIsLoading(false);
      }
  };

    const renderItem = ({ item }: { item: Message }) => (
    <View
    style={[
        styles.messageContainer,
        item.sender === 'user' ? styles.userMessage : styles.assistantMessage,
    ]}
    >
    {item.isLoading ? (
        <ActivityIndicator size="small" color="#4682B4" />
      ) : item.sender === 'assistant' ? (
      <Markdown
      style={{
        heading1: { color: "darkblue", fontSize: 20 },
        heading2: { color: "black", fontSize: 18 },
        body: { color: "black", fontSize: 16 },
        link: { color: "blue" },
        code_block: { backgroundColor: "eee", padding: 10 },
      }}
    >{item.text}</Markdown>
    ) : (
        <Text style={styles.messageText}>{item.text}</Text>
    )}
    </View>
  );

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      keyboardVerticalOffset={Platform.OS === 'ios' ? 90 : 0}
    >
      <FlatList
        data={messages}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
        ref={flatListRef}
        contentContainerStyle={styles.messagesList}
      />

      {/* O container do input está posicionado no final da árvore, permitindo que o KeyboardAvoidingView o mova */}
      <View style={styles.inputContainer}>
        <TextInput
            style={styles.input}
            placeholder="Digite sua mensagem..."
            value={inputText}
            onChangeText={setInputText}
            keyboardType="default" // Pode ser 'default', 'numeric', 'email-address', 'phone-pad', etc.
            autoFocus={true} // Para garantir que o campo de input tenha foco
        />
        <TouchableOpacity style={styles.sendButton} onPress={sendMessage}>
          <Ionicons name="send" size={24} color="#fff" />
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f2f2f2',
  },
  messagesList: {
    padding: 10,
    paddingBottom: 80, // Garante espaço para o campo de input
  },
  messageContainer: {
    maxWidth: '90%',
    padding: 10,
    marginBottom: 10,
    borderRadius: 10,
  },
  userMessage: {
    backgroundColor: '#87CEFA',
    alignSelf: 'flex-end',
    borderBottomRightRadius: 0,
    borderRadius: 20,
  },
  assistantMessage: {
    backgroundColor: '#fff',
    alignSelf: 'flex-start',
    borderBottomLeftRadius: 0,
    borderRadius: 20,
  },
  messageText: {
    fontSize: 16,
    color: '#333',
  },
  inputContainer: {
    flexDirection: 'row',
    paddingHorizontal: 10,
    paddingVertical: 8,
    backgroundColor: '#fff',
    alignItems: 'center',
    borderTopWidth: 1,
    borderColor: '#ccc',
  },
  input: {
    flex: 1,
    height: 40,
    backgroundColor: '#f2f2f2',
    borderRadius: 20,
    paddingHorizontal: 15,
    fontSize: 16,
    marginRight: 10,
  },
  sendButton: {
    backgroundColor: '#4682B4',
    width: 40,
    height: 40,
    borderRadius: 20,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

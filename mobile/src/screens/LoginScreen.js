import React from 'react';
import { View, Text, TextInput, Button } from 'react-native';

export default function LoginScreen({ navigation }) {
  return (
    <View style={{ padding: 16, gap: 10 }}>
      <Text style={{ fontSize: 24 }}>Login / Signup</Text>
      <TextInput placeholder="Email" style={{ borderWidth: 1, padding: 8 }} />
      <TextInput placeholder="Password" secureTextEntry style={{ borderWidth: 1, padding: 8 }} />
      <Button title="Continue" onPress={() => navigation.navigate('Browse')} />
    </View>
  );
}

import React from 'react';
import { View, Text, Button } from 'react-native';

export default function PaymentScreen({ navigation }) {
  return (
    <View style={{ padding: 16, gap: 10 }}>
      <Text style={{ fontSize: 24 }}>Payment</Text>
      <Text>Razorpay integration placeholder.</Text>
      <Button title="View Profile" onPress={() => navigation.navigate('Profile')} />
    </View>
  );
}

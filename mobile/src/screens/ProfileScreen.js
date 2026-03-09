import React from 'react';
import { View, Text } from 'react-native';

export default function ProfileScreen() {
  return (
    <View style={{ padding: 16, gap: 10 }}>
      <Text style={{ fontSize: 24 }}>Profile</Text>
      <Text>Booking history, ratings, and account settings.</Text>
    </View>
  );
}

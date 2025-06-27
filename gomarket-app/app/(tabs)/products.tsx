import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, ActivityIndicator } from 'react-native';
import axios from 'axios';

export default function ProductsScreen(){
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('http://localhost:8000/products/')
        .then(response => {
            setProducts(response.data);
        })
        .catch(error => {
            console.error('Erro ao buscar os produtos', error);
        })
        .finally(() => {setLoading(false)})
    }, []);

    if(loading) return <ActivityIndicator size="large" color="#0000ff" />;
    return (
        <View style={{flex: 1, padding: 20}}>
            <FlatList 
            data={products}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({item}) => (
                <View style={{marginBottom: 20}}>
                    <Text style={{fontSize: 18, fontWeight: 'bold'}}>{item.name}</Text>
                    <Text>{item.brand}</Text>
                    <Text>Preço: R$ {item.category}</Text>
                </View>
            )}
        />
        </View>
    );
}

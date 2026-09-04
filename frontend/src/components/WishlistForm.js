import React, { useState } from 'react';

export default function WishlistForm() {
    const [formData, setFormData] = useState({ name: '', item_names: '', priority: 'Medium', item_link: '' });
    const [status, setStatus] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch('http://localhost:8000/submit-wishlist', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData),
            });
            if (res.ok) setStatus('Wishlist sent successfully!');
            else setStatus('Error sending wishlist.');
        } catch (err) { setStatus('Network error.'); }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div style={{ marginBottom: '10px' }}>
                <label>Name: </label>
                <input placeholder="Name" onChange={e => setFormData({...formData, name: e.target.value})} required />
            </div>
            <div style={{ marginBottom: '10px' }}>
                <label>Item Names: </label>
                <textarea placeholder="Item Names" onChange={e => setFormData({...formData, item_names: e.target.value})} required />
            </div>
            <div style={{ marginBottom: '10px' }}>
                <label>Priority: </label>
                <select onChange={e => setFormData({...formData, priority: e.target.value})}>
                    <option value="High">High</option>
                    <option value="Medium">Medium</option>
                    <option value="Low">Low</option>
                </select>
            </div>
            <div style={{ marginBottom: '10px' }}>
                <label>Item Link: </label>
                <input placeholder="Item Link" type="url" onChange={e => setFormData({...formData, item_link: e.target.value})} required />
            </div>
            <button type="submit">Submit</button>
            <p>{status}</p>
        </form>
    );
}

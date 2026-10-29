import React, { useState } from 'react';

export default function WishlistForm() {
    const [formData, setFormData] = useState({ name: '', item_names: '', priority: 'Medium', item_link: '' });
    const [status, setStatus] = useState({ message: '', type: '' });
    const [isSubmitted, setIsSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatus({ message: 'Sending...', type: '' });
        try {
            const res = await fetch('http://localhost:8000/submit-wishlist', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData),
            });
            if (res.ok) {
                setIsSubmitted(true);
                setStatus({ message: 'Wishlist sent successfully!', type: 'success' });
            } else {
                setStatus({ message: 'Error sending wishlist.', type: 'error' });
            }
        } catch (err) { setStatus({ message: 'Network error. Is the backend running?', type: 'error' }); }
    };

    if (isSubmitted) {
        return (
            <div style={{ textAlign: 'center', padding: '2rem' }}>
                <h2 style={{ color: '#28a745' }}>🎉 Success!</h2>
                <p>Your wish list has been sent. Thank you!</p>
                <button onClick={() => setIsSubmitted(false)} style={{ marginTop: '1rem' }}>Send Another</button>
            </div>
        );
    }

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label>Name</label>
                <input placeholder="Your Name" onChange={e => setFormData({...formData, name: e.target.value})} required />
            </div>
            <div className="form-group">
                <label>Items</label>
                <textarea placeholder="Enter items, one per line" onChange={e => setFormData({...formData, item_names: e.target.value})} required />
            </div>
            <div className="form-group">
                <label>Priority</label>
                <select onChange={e => setFormData({...formData, priority: e.target.value})}>
                    <option value="High">High</option>
                    <option value="Medium">Medium</option>
                    <option value="Low">Low</option>
                </select>
            </div>
            <div className="form-group">
                <label>Item Link</label>
                <input placeholder="https://..." type="url" onChange={e => setFormData({...formData, item_link: e.target.value})} required />
            </div>
            <button type="submit">Send Wish List</button>
            {status.message && <p className={`status ${status.type}`}>{status.message}</p>}
        </form>
    );
}

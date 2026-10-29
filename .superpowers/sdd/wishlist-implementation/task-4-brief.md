: Frontend Form Implementation

**Files:**
- Create: `frontend/package.json`
- Create: `frontend/src/App.js`
- Create: `frontend/src/components/WishlistForm.js`

**Interfaces:**
- Consumes: POST `/submit-wishlist` from backend.

- [ ] **Step 1: Create package.json** (minimal react setup)
- [ ] **Step 2: Implement WishlistForm component**
```jsx
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
            <input placeholder="Name" onChange={e => setFormData({...formData, name: e.target.value})} required />
            <textarea placeholder="Item Names" onChange={e => setFormData({...formData, item_names: e.target.value})} required />
            <select onChange={e => setFormData({...formData, priority: e.target.value})}>
                <option value="High">High</option>
                <option value="Medium">Medium</option>
                <option value="Low">Low</option>
            </select>
            <input placeholder="Item Link" type="url" onChange={e => setFormData({...formData, item_link: e.target.value})} required />
            <button type="submit">Submit</button>
            <p>{status}</p>
        </form>
    );
}
```
- [ ] **Step 3: Implement App.js to render WishlistForm**
- [ ] **Step 4: Commit**
```bash
git add frontend/
git commit -m "feat: implement react frontend form"
```


app.get('/user', (req, res) => {
    const username = String(req.query.username);

    db.collection('users').findOne({ username: username }, (err, user) => {
        if (err) throw err;
        res.json(user);
    });
});

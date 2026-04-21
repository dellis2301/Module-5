app.get('/profile/:userId', (req, res) => {
    if (req.user.id !== req.params.userId) {
        return res.status(403).send("Forbidden");
    }

    User.findById(req.params.userId, (err, user) => {
        if (err) return res.status(500).send(err);
        res.json(user);
    });
});

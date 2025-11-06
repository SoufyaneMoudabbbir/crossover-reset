# Contributing to CrossOver Trial Reset

Thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- macOS version and CrossOver version
- Error messages (if any)

### Suggesting Features

Feature requests are welcome! Please:
- Check if the feature already exists or is requested
- Explain the use case
- Describe the expected behavior

### Pull Requests

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/crossover-reset.git`
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Make your changes**
5. **Test thoroughly** on macOS
6. **Commit**: `git commit -m "Add: your feature description"`
7. **Push**: `git push origin feature/your-feature-name`
8. **Open a Pull Request** with a clear description

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

### Testing

Before submitting:
- ✅ Test the app builds successfully
- ✅ Test on a real Mac (if possible)
- ✅ Verify no data loss occurs
- ✅ Check error handling works

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/crossover-reset.git
cd crossover-reset

# Make scripts executable
chmod +x build.sh check_ready.py

# Check requirements
./check_ready.py

# Build and test
./build.sh
open "dist/CrossOver Reset.app"
```

## Questions?

Feel free to open an issue for questions or join discussions!

---

**Thank you for contributing!** ❤️

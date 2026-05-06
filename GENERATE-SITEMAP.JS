name: Vulture Factory Orchestrator

on:
  schedule:
    - cron: '0 13 * * *'
  workflow_dispatch:
    inputs:
      mode:
        description: "Run mode"
        default: "full"
        type: choice
        options: [full, generate-only, deploy-only]
      force_rebuild:
        description: "Force rebuild"
        default: false
        type: boolean

jobs:
  orchestrator:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Force Install Dependencies
        run: |
          echo "Installing with legacy peer resolution..."
          # This flag bypasses the exact ERESOLVE error you just hit
          npm install --legacy-peer-deps || (
            echo "⚠️ Standard install failed, forcing clean slate..."
            npm cache clean --force
            rm -rf node_modules
            npm install --legacy-peer-deps --force
          )

      - name: Execution with Self-Healing Loop
        run: |
          MAX_RETRIES=3
          COUNT=1
          SUCCESS=false
          
          while [ $COUNT -le $MAX_RETRIES ]; do
            echo "Attempt $COUNT of $MAX_RETRIES..."
            # Using the inputs with safe shell defaults
            if node vulture-orchestrator.js --mode=${{ github.event.inputs.mode || 'full' }} --force=${{ github.event.inputs.force_rebuild || 'false' }}; then
              echo "✅ Orchestrator Success!"
              SUCCESS=true
              break
            else
              echo "⚠️ Attempt $COUNT failed. Running recovery..."
              # Target specific Vulture cache corruption
              rm -rf node_modules/.cache
              [ -f "vulture-repair-tool.js" ] && node vulture-repair-tool.js
              
              COUNT=$((COUNT+1))
              sleep 5
            fi
          done

          if [ "$SUCCESS" = false ]; then
            echo "❌ Final failure after $MAX_RETRIES attempts."
            exit 1
          fi
